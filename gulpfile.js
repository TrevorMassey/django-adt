var gulp = require('gulp'),
    //webpack = require('gulp-webpack'),
    source = require('vinyl-source-stream'),
    path = require('path'),
    config = require('./gulp.config')();
var _ = require('lodash');

var webpack = require('./webpack.config.js');

var gulpPlugin = require('gulp-load-plugins')({lazy: false});

/** Angular app js files **/
gulp.task('appJs', function () {
    return gulp.src(config.jsOrder)
        //.pipe(gulpPlugin.uglify({
        //  mangle: false,
        //compress: false
        //}))
        .pipe(gulpPlugin.concatUtil('application.js'))
        .pipe(gulp.dest(config.frontend.scripts));
});

/** Angular templates which are called in views and directives **/
gulp.task('templates', function () {
    return gulp.src(config.views.all)
        .pipe(gulpPlugin.angularTemplatecache('templates.js', {
            standalone: true,
            base: function (file) {
                return '/' + path.basename(file.relative);
            }
        }))
        .pipe(gulp.dest(config.frontend.scripts));
});


gulp.task('web-pack', ['scripts'], function() {
    return gulp.src(config.main)
        .pipe(gulpPlugin.webpack(webpack))
        .pipe(gulp.dest(config.frontend.scripts));
});


var filestoWatch = _.flatten([config.views.all, config.js, config.lessDir]);
console.log(filestoWatch);
gulp.task('watch', function() {
    return gulp.watch(filestoWatch, ['web-pack']);
    //return gulp.src(filestoWatch)
        //.pipe(gulpPlugin.webpack(_.assign({}, webpack, { watch: true })))
        //.pipe(gulp.dest(config.frontend.scripts));
});

/** Runs all application js tasks */
gulp.task('scripts', ['appJs', 'templates']);

gulp.task('default', ['web-pack', 'watch']);