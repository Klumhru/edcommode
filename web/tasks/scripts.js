
module.exports = function(gulp) {

  gulp.task('scripts', function() {
    var gutil = gulp.plugin.util,
        prod  = gutil.env.prod,
        Notification = require('node-notifier'),
        notifier = new Notification(),
        map = require('map-stream');


    return gulp.src(['./src/apps/**/*.js'])
      .pipe( gulp.plugin.plumber() )
      .pipe( prod || !gulp.waitingForBower ? gutil.noop() : gulp.plugin.changed('./dev/') )

      .pipe(
        true ? gutil.noop() : gulp.plugin.uglify({preserveComments: 'some'})
       )
      .pipe( gulp.dest(prod ? './dist/' : './dev/') )
      .pipe( prod ? gutil.noop() : gulp.plugin.connect.reload() );
  });

};
