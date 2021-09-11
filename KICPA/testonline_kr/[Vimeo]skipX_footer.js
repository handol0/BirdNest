$(function() {
    var iframe = $('#video1')[0];
    var player = $f(iframe);
    var status = $('.status');
    var playing = false;
    var simulationTime = 0;
  
    window.setInterval(function() {
      if (playing) {
        simulationTime++;
      }
    }, 1000)
    
    // When the player is `ready, add listeners for pause, finish, and playProgress
    player.addEvent('ready', function() {
        status.text('ready');
        player.addEvent('play', onPlay);
        player.addEvent('pause', onPause);
        player.addEvent('finish', onFinish);
        player.addEvent('seek', onSeek);
        player.addEvent('playProgress', onPlayProgress);
    });

    function onPlay(id) {
      playing = true;
    } 
  
    function onPause(id) {
      playing = false;
    }

    function onFinish(id) {
        status.text('finished, Credit Get!!');
    }

    function onSeek(data, id) {
      if (data.seconds > simulationTime) { 
        player.api('seekTo', Math.floor(simulationTime));
      }
      else {
        simulationTime = data.seconds;
      }       
    }
  
    function onPlayProgress(data, id) {
      status.text(data.seconds + 's played and simulation Time is '+ simulationTime);      
    }
});
