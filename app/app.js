'use strict';

/* App Module */

var myApp = angular.module('myApp', [
]);

var MyCtrl = function($scope, $log, $http) {
  $scope.cmd = "pwd \nls";
  $scope.output = "the output";

  $scope.execute = function(cmd) {
    $http.post('/bliss2', cmd)
    .success(function(data, status, headers, config) {
      $scope.output = "OK " + status + "\n" + data;
    })
    .error(function(data, status, headers, config) {
      $scope.output = "ERROR " + status + "\n" + data;
    });

    $scope.output = "I ran " + cmd;
  }

  $scope.onkey = function(evt) {
    if (evt.keyCode == 13) {
      $scope.execute($scope.cmd);
    }
  }
}
