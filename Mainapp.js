"use strict";
exports.__esModule = true;
var EmailValidator_1 = require("./EmailValidator");
var email = 'jenifery1486mail.com';
var validator = new EmailValidator_1.Emailvalidator();
var result = validator.isValid(email);
console.log(result);
