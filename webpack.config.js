// Add WebPack to use the included CommonsChunkPlugin
var webpack = require('webpack');
var ExtractTextPlugin = require("extract-text-webpack-plugin");

var config = {
  debug: true,

  addVendor: function (name, path) {
    this.resolve.alias[name] = path;
    this.module.noParse.push(new RegExp(path));
  },

  entry: {
    app: ['./frontend/src/main.js'],
    vendors: [
      'lodash',
      'angular',
      'angular-resource',
      'angular-messages',
      'angular-animate',
      'angular-ui-router',
      'satellizer',
      'restangular'
    ]
  },
  resolve: {
    extensions: ['', '.js']
  },
  output: {
    path: __dirname + '/frontend/static/scripts',
    filename: "main.js"
  },

  module: {
    loaders: [
      //{ test: /\.html$/, loader: 'file-loader' },
      { test: /\.css/, loader: 'style!css' },
      { test: /\.less$/, loader: 'style!css!less' },
      { test: /\.jpe?g$|\.gif$|\.png$|\.wav$|\.mp3$/, loader: 'url' },
      { test: /\.svg$|\.woff$|\.woff2$|\.eot$|\.ttf$/, loader: 'url-loader?limit=100000' }

      //setup later for production
      //{ test: /\.less$/, loader: ExtractTextPlugin.extract('style-loader', 'less-loader') }
    ]
  },
  plugins: [

    // We add a plugin called CommonsChunkPlugin that will take the vendors chunk
    // and create a vendors.js file. As you can see the first argument matches the key
    // of the entry, "vendors"
    new webpack.optimize.CommonsChunkPlugin('vendors', 'vendors.js'),

    //setup later for production
    //new ExtractTextPlugin("[name].css")
  ]
};

//config.addVendor('bootstrap', bower_dir + '/bootstrap/bootstrap.min.js');
//config.addVendor('bootstrap.css', bower_dir + '/bootstrap/bootstrap.min.css');

module.exports = config;