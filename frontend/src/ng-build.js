module.exports = function() {
    require('angular-strap/dist/angular-strap.min.js');
    require('angular-strap/dist/angular-strap.tpl.min.js');

    require('rx-angular');
    require('angular-moment');
    require('angular-breadcrumb');
    require('angular-loading-bar');
    require('angular-toastr');
    require('angular-toastr/dist/angular-toastr.css');

    //TODO: (remove from index.html) currently have swampdragon service included from index.html
    //require('./swampdragon/dist/services.js');
};