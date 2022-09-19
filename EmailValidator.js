"use strict";
exports.__esModule = true;
exports.Emailvalidator = void 0;
var Emailvalidator = /** @class */ (function () {
    function Emailvalidator() {
    }
    Emailvalidator.prototype.isValid = function (s) {
        var EmailRegEx = /^[a-z0-9]+@[a-z]+\.[a-z]{2,3}/;
        return EmailRegEx.test(s);
    };
    return Emailvalidator;
}());
exports.Emailvalidator = Emailvalidator;
