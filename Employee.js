var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var Employee = /** @class */ (function () {
    function Employee(fname, lname) {
        this.fname = fname;
        this.lname = lname;
    }
    Employee.prototype.compensationStatement = function () {
        return "".concat(this.fname, " makes ").concat(this.getSalary(), " for a month in the year 2021-2022");
    };
    return Employee;
}());
var FullTimeEmployee = /** @class */ (function (_super) {
    __extends(FullTimeEmployee, _super);
    function FullTimeEmployee(fname, lname, salary) {
        var _this = _super.call(this, fname, lname) || this;
        _this.salary = salary;
        return _this;
    }
    FullTimeEmployee.prototype.getSalary = function () {
        return this.salary;
    };
    return FullTimeEmployee;
}(Employee));
var ContractEmployee = /** @class */ (function (_super) {
    __extends(ContractEmployee, _super);
    function ContractEmployee(fname, lname, rate, hours) {
        var _this = _super.call(this, fname, lname) || this;
        _this.rate = rate;
        _this.hours = hours;
        return _this;
    }
    ContractEmployee.prototype.getSalary = function () {
        return this.rate * this.hours;
    };
    return ContractEmployee;
}(Employee));
var emp1 = new FullTimeEmployee("Amy", "Jackson", 25000);
console.log(emp1.compensationStatement());
var cemp1 = new ContractEmployee("Alex", "Immanuel", 1500, 8);
console.log(cemp1.compensationStatement());
