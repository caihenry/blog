!function(a){var e=0;a.jstars={},a.fn.jstars=function(t){var s=window.navigator.userAgent,r=s.indexOf("MSIE ");if(!(r>0&&parseInt(s.substring(r+5,s.indexOf(".",r)))<9)){(t=a.extend({},a.fn.jstars.defaults,t)).frequency=20-Math.max(1,Math.min(t.frequency,19));var i=null,p=0,o=0,l=null,u="jstar_span_"+e++;return this.each(function(){if(!i){i=setInterval(function(){a("span.jstar_span").size&&a("span.jstar_span."+u).each(function(){var e=a(this).css("background-position").split(" "),n=parseInt(e[0]),s=parseInt(e[1]);a(this).css("background-position",n-t.width+"px "+s+"px")})},t.delay/9),(l=new Image).src=t.image_path+"/"+t.image}a(this).mousemove(function(e){if(o++%t.frequency==0){var s=n(-1,1),r=n(-1,1),i=n(5,30),d=n(5,30),c=Math.min(Math.random()+.4,1),f=e.pageX+s*i,h=e.pageY+r*d,m="jstar_"+p++;if("rand"!=t.style)var y="0px "+t.style_map[t.style]+"px";else{var g=n(0,5),v=0;for(var x in t.style_map)if(v++==g){y="0px "+t.style_map[x]+"px";break}}var _='<span id="'+m+'" class="jstar_span '+u+'" style="display:block; width:27px; height:27px; background:url('+l.src+") no-repeat "+y+'; margin:0; padding:0; position:absolute; top:-50px; left:0; pointer-events: none;">&nbsp;</span>';a(document.body).append(_);var j=a("#"+m);j.css({top:h,left:f,opacity:c}).animate({opacity:0},t.delay,function(){j.remove()})}})})}};function n(a,e){var n=Math.random();return n*=e-a,n+=a,n=Math.round(n)}a.fn.jstars.defaults={image_path:"",image:"jstar-modern.png",style:"white",frequency:12,style_map:{white:0,blue:-25,green:-50,red:-75,yellow:-100},width:25,height:25,delay:500}}(jQuery);