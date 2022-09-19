class Person{
    private _age:number;
    public _fname:string;
    public _lname:string;
    

    constructor(fname :string,lname:string)
    {
        this._fname=fname;
        this._lname=lname;
    }


    public get age()
    {
         return this._age;
    }
    public set age(myAge:number)
    {
        if(myAge <=0 || myAge>=100)
        {
            throw new Error("Enter a valid age");
        }
          
        this._age=myAge;
    }

    public display():string{
        return `${this._fname} ${this._lname}}`;
    }

}
let person1=new Person("John","doe");
person1.age=10;
console.log(person1.age);