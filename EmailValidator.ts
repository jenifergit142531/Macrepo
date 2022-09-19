import { validator } from "./Validator";

export class Emailvalidator implements validator{
    isValid(s: string): boolean {
        const EmailRegEx=/^[a-z0-9]+@[a-z]+\.[a-z]{2,3}/;
        return EmailRegEx.test(s);
    }
}




