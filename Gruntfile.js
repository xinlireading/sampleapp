module.exports = function(grunt) {
    grunt.initConfig({
        cssmin: {
            target: {
                files: [{
                    src: 'polls/static/polls/css/*.css',
                    dest: 'polls/static/polls/css/',
                    expand: true,
                    flatten: true,
                    ext: '.min.css'
                }]
            },
            options: {
              sourceMap: true,
            }
        }
    });
    // grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-cssmin');
    grunt.registerTask('default', ['cssmin']);
};
