'use strict';

module.exports = function(gulp) {

  gulp.task('bower', function() {
    var mainBowerFiles = require('main-bower-files');

    var jsFilter = gulp.plugin.filter(['**/*.js','**/*.map']),
        imgFilter = gulp.plugin.filter('**/*.{png,gif,jpg,jpeg,svg}'),
        cssFilter = gulp.plugin.filter('**/*.css'),
        scssFilter = gulp.plugin.filter('**/*.scss'),
        fontFilter = gulp.plugin.filter('**/*.otf');

    gulp.src(['bower_components/foundation/scss/**/*.scss',
              'bower_components/foundation-icon-fonts/*(*.ttf|*.otf|*.eot|*.woff|*.svg)',
              'bower_components/foundation-icon-fonts/_foundation-icons.scss'])
        .pipe(gulp.dest('./src/style/vendor/'));

    return gulp.src(mainBowerFiles())
      .pipe( jsFilter )
      .pipe( gulp.dest('./src/apps/vendor/') )
      .pipe( jsFilter.restore() )

      .pipe( imgFilter )
      .pipe( gulp.dest('./src/style/img/vendor/') )
      .pipe( imgFilter.restore() )

      .pipe( cssFilter )
      .pipe( gulp.plugin.rename({extname: '.scss'}) )
      .pipe( cssFilter.restore() )

      .pipe( fontFilter )
      .pipe( gulp.dest('./src/style/vendor/') )
      .pipe( fontFilter.restore() )

      .pipe( scssFilter )
      .pipe( gulp.dest('./src/style/vendor/') )
      .pipe( scssFilter.restore() );
  });
};
