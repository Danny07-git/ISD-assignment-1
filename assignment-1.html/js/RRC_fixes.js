/**** v1.0 Released Feb 5 2019 ****/
/***  RRC Fixes and Overrides ***/

    // Detect the current width of each iframe's parent container
    // then set the iframe width the same as the parent's.
    // Height of the iframe is then set based on a 16:9 aspect ratio
    // relative to current width
    function scaleVid(){
    $('iframe').each(function() {
      // find iframe ht/wdth FROM HTML ATTRIBUTES (if it exists) to determine aspect ratio
      var frameHeight = $(this).attr('height');
      var frameWidth =  $(this).attr('width');
      var frameAR  =  frameWidth/frameHeight;

      if(frameAR <= 1.5){
        $width = $(this).parent().width(); //get the width from the parent container
        $height = ($width/4)*3; // calculate 4:3 Aspect ratio
      }
      else if(frameAR >= 1.5){
        $width = $(this).parent().width(); //get the width from the parent container
        $height = ($width/16)*9; // calculate 16:9 Aspect ratio
      }
      else{
        $width = $(this).parent().width(); //get the width from the parent container
        $height = ($width/16)*9; // calculate 16:9 Aspect ratio
      };

      $(this).attr({
        "height" : $height,
        "width" : $width
      });
    });
    };

    function fixWell(){
      var maxHeight = $('.well-icon').next().height();
      $('.well-icon').height(maxHeight);
    };

    // everytime the page is loaded, resized or scrolled make sure the
    // video behaves by running our fancy function
    $(window).on("load resize scroll",function(e){
      scaleVid();
      fixWell();
    });

/***** v1.1 Released May 1 2020 *****/
/***  RRC Fixes and Overrides ***/

    //PATCH for v1.1 and later PATCH
    const rrcTemplateVersion = document.querySelector('meta[name="description"]').content;
    if(rrcTemplateVersion !== "RRC_fixes v1.0"){
      //debug version
      //$("body").append('This is version 1.1 or higher');
      console.log(rrcTemplateVersion);

      //clean incorrect CSS from main.css & main.min.css
      $('.banner-img img').css({"height":"initial", "object-fit":"contain"});

      //shut off the NONSENSE that d2l's WYSIWYG inserts into a modified banner image
      $('.banner-img > img').attr({height:' ', width:' '});      
    }else{
      //debug version
      //$("body").append('This <strong>is</strong> version 1.0');
      console.log(rrcTemplateVersion);
    };