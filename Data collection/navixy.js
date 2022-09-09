const navixy = require('navixy-js-sdk');
const API = new navixy.Api({
    user:{
       login:'24621',
       password:'Cassilas@7'
    },
    domain:'24621.navixy.com'
})

API.tracker.list().then(list => console.log(list))
API.request('user/settings').then(settings => console.log(settings))