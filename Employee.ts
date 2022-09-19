abstract class Employee
{
    
    

    constructor(private fname:string,private lname:string)
    {
        
    }
    abstract getSalary():number;

    compensationStatement():string{
        return `${this.fname} makes ${this.getSalary()} for a month in the year 2021-2022`;
    }

}
class FullTimeEmployee extends Employee{

    constructor(fname:string,lname:string,private salary:number)
    {
        super(fname,lname);
    }

    getSalary(): number {
        return this.salary;
    }
}

class ContractEmployee extends Employee{

    constructor(fname:string,lname:string,private rate:number,private hours:number)
    {
        super(fname,lname);
    }
    
    getSalary(): number {
        return this.rate*this.hours;
    }
}


let emp1=new FullTimeEmployee("Amy","Jackson",25000);

console.log(emp1.compensationStatement());

let cemp1=new ContractEmployee("Alex","Immanuel",1500,8);

console.log (cemp1.compensationStatement());
