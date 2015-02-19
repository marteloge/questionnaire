var qs = qs || {};
qs.bindForm = function(bindings, id) {
  
  var createHandler = function(key, value) {
    $("#"+key).click(function() { // klikker på bilde
      $("#" + id).val(value);

      var src = $(this).attr('src');
      var src_selected = src.replace('.svg', '-selected.svg');

      //fjerner alle klasser og setter src til svart ikon
      $("#content-module").find('img').removeClass('selected');

      //Legger til klassen selected på bildet som ble klikket på
      $(this).addClass('selected');

      //Endrer valgt bilde til grønt
      $(this).attr("src",src_selected);

      //Fader ut skjermen
      $( "#wrapper").fadeOut( "slow", function() {
        $("#btn-post").click();
      });
    });
  };
  for (key in bindings) {
    createHandler(key, bindings[key]);
  }
};

function addNationality() {
  $('.dropdown').dropdown({
    onChange: function(val) {
      $('#id_nationality').val(val);
    },
    onShow: function() {
      $('#navigation').hide();
    },
    onHide: function() {
      $(document.activeElement).blur();
      $('#navigation').show();
    },
  });
  $('#submit_nationality').click(function() {
    $('#btn-post').click();
  });
}

function addPattern() {
  var start = new Date();
  var radius = 0.6*(screen.width/8);
  var margin = 0.2*(screen.width/4);

  var patternheight = radius*6 + margin*8;
  var availHeight = document.getElementById('content-module').clientHeight;

  if(patternheight > availHeight){
    radius = radius - radius*((patternheight/availHeight)-1);
    margin = margin - margin*((patternheight/availHeight)-1);
  }

  $('#continue').attr("disabled", true);
  $('#retry').attr("disabled", true);
  $('#retrypattern').attr("disabled", true);

  var lock = new PatternLock('#patternContainer', {
    onDraw:function(pattern){
      pattern = lock.getPattern();
      $('#message').removeClass('hidden');
      $('#message').text('Pattern recorded');
      
      if(pattern.length>=4 && validatePattern(pattern.split(''))){
        $('#retrypattern').click(function() {
          lock.reset();
          $('#message').addClass('hidden');
          $('#continue').attr("disabled", true);
          $('#retry').attr("disabled", true);
          $('#retrypattern').attr("disabled", true);
        });
        $('#continue').click(function() {
          var end = new Date();
          $('#id_sequence').val(pattern);
          $('#id_time').val(end-start);
          $( "#wrapper").fadeOut( "slow", function() {
            $('#btn-post-continue').click();
          });
        });
        $('#retry').click(function() {
          var end = new Date();
          $('#id_sequence').val(pattern);
          $('#id_time').val(end-start);
          $('#btn-post-retry').click();
          $('#continue').attr("disabled", true);
          $('#retry').attr("disabled", true);
          $('#retrypattern').attr("disabled", true);
        });
      }
      else {
        lock.error();
        
        if(validatePattern(pattern.split(''))==false){
          $('#message').text('Some of the selected dots was not recorded. Please retype the pattern :)');
        }
        else {
          $('#message').text('Connect at least 4 dots');
        }
        $('#message').removeClass('hidden');
        
        $('#retrypattern').click(function() {
          lock.reset();
          $('#message').addClass('hidden');

          $('#continue').attr("disabled", true);
          $('#retry').attr("disabled", true);
          $('#retrypattern').attr("disabled", true);
        });
        $('#retry').click(function() {
          lock.reset();
          $('#message').addClass('hidden');
          $('#continue').attr("disabled", true);
          $('#retry').attr("disabled", true);
          $('#retrypattern').attr("disabled", true);
        });
      }
    },
    radius: radius,
    margin: margin,
  });

}

//AndroidOS, BlackBerryOS, PalmOS, SymbianOS, WindowsMobileOS, WindowsPhoneOS, iOS, MeeGoOS, MaemoOS, JavaOS, webOS, badaOS, BREWOS
function getMobileOperatingSystem() {
    var md = new MobileDetect(window.navigator.userAgent);
    var os = md.os();
    $('#os_notfound').hide();
    $('#os_found').show();

    if(os==null){
      $('#os_notfound').show();
      $('#os_found').hide();
      $('.dropdown').dropdown({
        onChange: function(val) {
          $('#id_mobileOS').val(val);  
        }
      });
      $('#submitOS').click(function() {
        $('#btn-post').click();
      });
    }
    else if(os.match("iOS")) {
      $('img#yes').attr('id', 'ios');
      $('img#no').attr('id', 'no_ios');
      $('img#unknown').attr('id', 'unknown_ios');
      $('img#mobileOS').attr('src', '/static/images/icons/ios.svg');
      $('label#mobile-label').text('iOS (iPhone)');
    }
    else if(os.match("Android")) {
      $('img#yes').attr('id', 'android');
      $('img#no').attr('id', 'no_android');
      $('img#unknown').attr('id', 'unknown_android');
      $('img#mobileOS').attr('src', '/static/images/icons/android.svg');
      $('label#mobile-label').text('Android');
    }
    else if(os.match("BlackBerry")) {
      $('img#yes').attr('id', 'blackberry');
      $('img#no').attr('id', 'no_blackberry');
      $('img#unknown').attr('id', 'unknown_blackberry');
      $('img#mobileOS').attr('src', '/static/images/icons/blackberry.svg');
      $('label#mobile-label').text('BlackBerry');
    }
    else if(os.match("Windows")){
      $('img#yes').attr('id', 'windows');
      $('img#no').attr('id', 'no_windows');
      $('img#unknown').attr('id', 'unknown_windows');
      $('img#mobileOS').attr('src', '/static/images/icons/windows.svg');
      $('label#mobile-label').text('Windows');
    }
    else {
      $('#os_notfound').show();
      $('#os_found').hide();
      $('.dropdown').dropdown({
        onChange: function(val) {
          $('#id_mobileOS').val(val);  
        }
      });
      $('#submitOS').click(function() {
        $('#btn-post').click();
      });
    }
};

function addAge() {
    $('#submitAge').click(function() {
      $("#id_age").val($("#age").val());
      $('#btn-post').click();
    });
};

function setScreenSize() {
  $('#id_actual_screenheight').val(screen.width);
  $('#id_actual_screenwidth').val(screen.height);
  // $(window).width()
};

function fixedFooter() {
  $("#age").focus(function(){
    $('#navigation').hide();
  });
  $("#age").blur(function(){
    $('#navigation').show();
  });
};

var between = function between(n1, n2) {
 
  /* base case */
  if (n1 === n2) {
    return null;
  }
  
  /* decrease to make null-index */
  --n1;
  --n2;
  
  /* calculate the average of the two numbers */
  avg = (n1 + n2) / 2
 
 
  /* check if same row or column */
  if ((Math.floor(n1 / 3) == Math.floor(n2 / 3)) || n1 % 3 == n2 % 3) {
    /* it's on the same row/column, if average is whole number, return it */
    if (avg === Math.floor(avg)) {
      return avg + 1;
    } else {
      return null;
    }
  } else if (avg === Math.floor(avg)) {
    /* if average is whole number and not on row or column, we're on the diagonal */
    /* if the distance between the columns is larger than 1, the average is in between */
    if (Math.abs(n1 % 3 - n2 % 3) > 1) {
      return avg + 1
    }
  }
  return null;
 
}
var validatePattern = function validatePattern(pattern) {
  /* make sure everything is integers */ 
  var p = [];
  for (var i = 0; i < pattern.length; ++i) {
    p.push(parseInt(pattern[i]));
  }
  var visited = [];
  var b;
  for (var i = 0; i < p.length - 1; ++i) {
    visited.push(p[i]);
    b = between(p[i], p[i + 1]);
    if (b !== null && visited.indexOf(b) == -1) {
      return false;
    }
  }
  return true;
};

