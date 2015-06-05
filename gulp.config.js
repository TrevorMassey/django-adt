'use strict';

module.exports = function() {
    var srcRoot = './frontend/src';

    var config = {
        srcFiles: srcRoot,
        main: srcRoot + '/main.js',
        frontend: {
            scripts: './frontend/static/scripts',
            index: './frontend/static/index.html'
        },
        views: {
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
            srcRoot + '/js/webgl-shader.frag']
    };

    return config;
};