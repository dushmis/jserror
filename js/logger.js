(function() {
  window.onerror = function() {
    var b = arguments;
    if (-1 !== window.navigator.vendor.indexOf("Google") && JSON && JSON.stringify && "object" === typeof b) {
      var a = !1;
      window.XMLHttpRequest ? a = new XMLHttpRequest : window.ActiveXObject && (a = new ActiveXObject("Microsoft.XMLHTTP"));
      a && (a.open("POST", "http://gelogger.appspot.com/"), a.setRequestHeader("Content-Type", "application/x-www-form-urlencoded"), a.send("er=" + JSON.stringify(b)));
    }
  };
})();