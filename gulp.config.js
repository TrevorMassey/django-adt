'use strict';

module.exports = function() {
    var srcRoot = './frontend/src';

    var config = {
        main: srcRoot + '/main.js',
        frontend: {
            scripts: './frontend/static/scripts'
        },
        views: {
            index: srcRoot + '/index.html',
            all: srcRoot + '/app/**/*.html'
        },
        less : [srcRoot + '/less/addiction-theme.less'],
        lessDir : [srcRoot + '/less/*.less'],
        fonts: [srcRoot + '/fonts/*'],
        js : [
            srcRoot + '/app/**/*.js'
        ],
        jsOrder: [
            srcRoot + '/ng-custom/*.js',
            srcRoot + '/app/*.js',
            srcRoot + '/app/**/*.module.js',
            srcRoot + '/app/**/*.js'
        ],
        webGLScripts: [
            srcRoot +'/js/*.js',
            srcRoot + '/js/webgl-shader.frag'],

        //Directories to copy into or inject from into index.html
        temp: {
            root: './.tmp',
            index: './.tmp/index.html',
            styles: './.tmp/css/',
            scripts : './.tmp/scripts/',
            css : ['./.tmp/**/*.css'],
            fonts : './.tmp/fonts/',

            //inject into index.html
            ngScripts : ['./.tmp/**/*.js']
        }
    };

    return config;
};