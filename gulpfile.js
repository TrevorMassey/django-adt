var gulp = require('gulp'),
    webpack = require('gulp-webpack'),
    source = require('vinyl-source-stream'),
    path = require('path'),
    config = require('./gulp.config')();

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
        .pipe(webpack( require('./webpack.config.js') ))
        .pipe(gulp.dest(config.frontend.scripts));
});

gulp.task('watch', function() {
    gulp.watch([config.js], ['web-pack']);
    gulp.watch([config.views.all], ['web-pack']);
});

/** Runs all application js tasks */
gulp.task('scripts', ['appJs', 'templates']);

gulp.task('default', ['web-pack', 'watch']);