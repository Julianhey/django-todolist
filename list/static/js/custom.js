/**
 * Created by s157570 on 3-12-2016.
 */

$(document).ready(function() {
    $('#media').hide();
    $('#review').hide();
    $('#forum').hide();

    $('#mediabutton').on('click', function () {
        $('#media').toggle();

    });

    $('#reviewbutton').on('click', function () {
        $('#review').toggle();

    });
    $('#forumbutton').on('click', function () {
        $('#forum').toggle();

    });

});