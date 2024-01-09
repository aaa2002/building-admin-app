const express = require('express');
const http = require('http');
const socketIO = require('socket.io');
const cors = require('cors');
const { MongoClient, ServerApiVersion } = require('mongodb');

const app = express();
const server = http.createServer(app);

const uri = "mongodb+srv://aaa2002:aaa@rest-api-shop.mfayt2v.mongodb.net/?retryWrites=true&w=majority";

app.use(cors());

const io = socketIO(server, {
  cors: {
    origin: "*",
    methods: ["GET", "POST", "PUT", "DELETE", "HEAD", "PATCH"],
    credentials: true
  }
});

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

// MongoDB connection
const client = new MongoClient(uri, {
  serverApi: {
    version: ServerApiVersion.v1,
    strict: true,
    deprecationErrors: true,
  }
});

async function run() {
  try {
    // Connect to MongoDB
    await client.connect();
    console.log("Connected to MongoDB");

    // Use the specific database and collection you want to store the chat messages
    const database = client.db("chat_messages");
    const messagesCollection = database.collection("test");
    /// TODO: name collections like senderId-receiverId

    io.on('connection', (socket) => {
      console.log('A user connected');

      socket.on('chat message', async (msg) => {
        console.log('Received message:', msg);
        
        // Save the message to MongoDB
        await messagesCollection.insertOne({
            /// TODO: Add the user information here
            /// sender: senderId,
            /// receiver: receiverId,
          user: socket.id, // You might want to replace this with the actual user information
          message: msg,
          timestamp: new Date(),
        });

        // Broadcast the message to all connected clients
        io.emit('chat message', msg);
      });

      socket.on('disconnect', () => {
        console.log('User disconnected');
      });
    });
  } finally {
    // Ensure that the client will close when you finish/error
    // Commenting this out to keep the MongoDB connection open while the server is running
    // await client.close();
  }
}

// Start the server
const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});

// Run the MongoDB connection
run().catch(console.dir);
