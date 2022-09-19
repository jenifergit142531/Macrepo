var Person = /** @class */ (function () {
    function Person(fname, lname) {
        this._fname = fname;
        this._lname = lname;
    }
    Object.defineProperty(Person.prototype, "age", {
        get: function () {
            return this._age;
        },
        set: function (myAge) {
            if (myAge <= 0 || myAge >= 100) {
                throw new Error("Enter a valid age");
            }
            this._age = myAge;
        },
        enumerable: false,
        configurable: true
    });
    Person.prototype.display = function () {
        return "".concat(this._fname, " ").concat(this._lname, "}");
    };
    return Person;
}());
var person1 = new Person("John", "doe");
person1.age = 10;
console.log(person1.age);
