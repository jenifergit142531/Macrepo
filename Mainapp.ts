import { Emailvalidator } from './EmailValidator';

let email='jenifery1486mail.com';
let validator=new Emailvalidator();
let result = validator.isValid(email);

console.log(result);