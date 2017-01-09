/**
 * Created by s157570 on 3-12-2016.
 */

$(document).ready(function() {

    var fieldparams = 'name,summary,first_release_date)'

    $('.list-group-item').on('click', function () {

    var gamename = $(this).text();

    $.ajax({
    url: 'https://igdbcom-internet-game-database-v1.p.mashape.com/games/', // The URL to the API. You can get this by clicking on "Show CURL example" from an API profile
    type: 'GET', // The HTTP Method
    data: {'search': gamename,
            'fields': fieldparams,
            'limit': 1}, // Additional parameters here
    datatype: 'json',
    success: function(data) { $('#infopname').html(data[0].name)
                              $('#infopsum').html(data[0].summary)
                              $('#infopdate').html(data[0].first_release_date)},   //alert(JSON.stringify(data));
    error: function(err) { alert(err); },
    beforeSend: function(xhr) {
    xhr.setRequestHeader("X-Mashape-Authorization", "0oFh6CBgQDmsh4M7zsMvWXLtAfyap13eWAwjsnvo3Rxt6StIyb"); // Enter here your Mashape key
    }
    });
  });


});
