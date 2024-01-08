import { createStore } from 'vuex';
import axios from "axios";

export default createStore({
  state: {
    apartments: [
      {
        id: 1,
        building: {
          id: 1,
          address: 'Cluj-Napoca, str. Gheorghe Doja, nr. 1',
          admin: 'Admin 1',
          neighbourhood: 'Gheorgheni',
          lat: 46.745899,
          lng: 23.484609,
        },
        name: 'Apartment 1',
        location: 'Location 1',
        price: 1000,
        bedrooms: 1,
        bathrooms: 1,
        area: 100,
        image: 'https://via.placeholder.com/150',
        description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla aliquet, diam eget molestie ultricies, nisl elit aliquet nunc, eu aliqu'
      },
      {
        id: 2,
        building: {
          id: 1,
          address: 'Cluj-Napoca, str. Gheorghe Doja, nr. 1',
          admin: 'Admin 1',
          neighbourhood: 'Gheorgheni',
          lat: 46.745899,
          lng: 23.484609,
        },
        name: 'Apartment 2',
        location: 'Location 1',
        price: 1000,
        bedrooms: 1,
        bathrooms: 1,
        area: 100,
        image: 'https://via.placeholder.com/150',
        description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla aliquet, diam eget molestie ultricies, nisl elit aliquet nunc, eu aliqu'
      },
      {
        id: 3,
        building: {
          id: 2,
          address: 'Cluj-Napoca, str. Observatorului, nr. 1',
          admin: 'Admin 1',
          neighbourhood: 'Observator',
          lat: 46.7712,
          lng: 23.6236,
        },
        name: 'Apartment 3',
        location: 'Location 1',
        price: 1000,
        bedrooms: 1,
        bathrooms: 1,
        area: 100,
        image: 'https://via.placeholder.com/150',
        description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla aliquet, diam eget molestie ultricies, nisl elit aliquet nunc, eu aliqu'
      },
      {
        id: 4,
        building: {
          id: 2,
          address: 'Cluj-Napoca, str. Observatorului, nr. 1',
          admin: 'Admin 1',
          neighbourhood: 'Observator',
          lat: 46.7712,
          lng: 23.6236,
        },
        name: 'Apartment 4',
        location: 'Location 1',
        price: 1000,
        bedrooms: 1,
        bathrooms: 1,
        area: 100,
        image: 'https://via.placeholder.com/150',
        description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla aliquet, diam eget molestie ultricies, nisl elit aliquet nunc, eu aliqu'
      },
      {
        id: 5,
        building: {
          id: 2,
          address: 'Cluj-Napoca, str. Observatorului, nr. 1',
          admin: 'Admin 1',
          neighbourhood: 'Observator',
          lat: 46.7712,
          lng: 23.6236,
        },
        name: 'Apartment 5',
        location: 'Location 1',
        price: 1000,
        bedrooms: 1,
        bathrooms: 1,
        area: 100,
        image: 'https://via.placeholder.com/150',
        description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla aliquet, diam eget molestie ultricies, nisl elit aliquet nunc, eu aliqu'
      },
      {
        id: 6,
        building: {
          id: 2,
          address: 'Cluj-Napoca, str. Observatorului, nr. 1',
          admin: 'Admin 1',
          neighbourhood: 'Observator',
          lat: 46.7712,
          lng: 23.6236,
        },
        name: 'Apartment 6',
        location: 'Location 1',
        price: 1000,
        bedrooms: 1,
        bathrooms: 1,
        area: 100,
        image: 'https://via.placeholder.com/150',
        description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla aliquet, diam eget molestie ultricies, nisl elit aliquet nunc, eu aliqu'
      },
      {
        id: 7,
        building: {
          id: 2,
          address: 'Cluj-Napoca, str. Observatorului, nr. 1',
          admin: 'Admin 1',
          neighbourhood: 'Observator',
          lat: 46.7712,
          lng: 23.6236,
        },
        name: 'Apartmen 7',
        location: 'Location 1',
        price: 1000,
        bedrooms: 1,
        bathrooms: 1,
        area: 100,
        image: 'https://via.placeholder.com/150',
        description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla aliquet, diam eget molestie ultricies, nisl elit aliquet nunc, eu aliqu'
      },
      {
        id: 8,
        building: {
          id: 2,
          address: 'Cluj-Napoca, str. Observatorului, nr. 1',
          admin: 'Admin 1',
          neighbourhood: 'Observator',
          lat: 46.7712,
          lng: 23.6236,
        },
        name: 'Apartment 8',
        location: 'Location 1',
        price: 1000,
        bedrooms: 1,
        bathrooms: 1,
        area: 100,
        image: 'https://via.placeholder.com/150',
        description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla aliquet, diam eget molestie ultricies, nisl elit aliquet nunc, eu aliqu'
      },

    ],

    user: {
      isAuthenticated: false,
      id: null,
      name: null,
      email: null,
      is_staff: false,
      refresh: null,
    }
  },
  getters: {
  },
  mutations: {
    setToken(state, data) {
      console.log('setToken', data);
      state.user.access = data.access;
      state.user.refresh = data.refresh;
      state.user.isAuthenticated = true;

      localStorage.setItem('user.access', data.access);
      localStorage.setItem('user.refresh', data.refresh);
      console.log('user.access: ', localStorage.getItem('user.access'))
    },

    removeToken(state) {
      console.log('removeToken');
      state.user.refresh = null;
      state.user.access = null;
      state.user.isAuthenticated = false;
      state.user.id = null;
      state.user.name = null;
      state.user.email = null;
      localStorage.setItem('user.access', '');
      localStorage.setItem('user.refresh', '');
      localStorage.setItem('user.id', '');
      localStorage.setItem('user.name', '');
      localStorage.setItem('user.email', '');
    },

    setUserInfo(state, user) {
      console.log('setUserInfo', user);
      state.user.id = user.id;
      state.user.name = user.name;
      state.user.email = user.email;
      state.user.is_staff = user.is_staff;
      localStorage.setItem('user.id', state.user.id);
      localStorage.setItem('user.name', state.user.name);
      localStorage.setItem('user.email', state.user.email);
      localStorage.setItem('user.is_staff', state.user.is_staff);
      console.log('User', state.user);
    },

    initStore(state){
      if (localStorage.getItem('user.access')) {
        console.log('Init user:', state.user);
        state.user.access  = localStorage.getItem('user.access');
        state.user.refresh = localStorage.getItem('user.refresh');
        //state.dispatch('refreshToken');
      }else{
        state.user.access = ''
        state.isAuthenticated = true
      }
    },

    refreshToken(state) {
      axios.post('/api/refresh/', {
        refresh: state.user.refresh,
      })
        .then((response) => {
          state.commit('setToken', {
            access: response.data.access,
            refresh: state.user.refresh,
          });
          axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access;
        })
        .catch((error) => {
          console.log(error);
          state.commit('removeToken');
        });
      },
  },
  actions: {
    setToken(context, data){
      context.commit('setToken',data)
    },


    setUserInfo(context, user) {
      context.setUserInfo.commit('setUserInfo',user)
    },
    
    refreshToken(context) {
      axios.post('/api/refresh/', {
        refresh: context.state.user.refresh,
      })
        .then((response) => {
          context.commit('setToken', {
            access: response.data.access,
            refresh: context.state.user.refresh,
          });
          axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access;
        })
        .catch((error) => {
          console.log(error);
          context.commit('removeToken');
        });
    },
  },
  modules: {
  }
})
