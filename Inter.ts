
interface Movies
{
    getBollywood():string;
    getHollywood():string;

}


class HindiAudience implements Movies{

getHollywood(): string {
    return "not interested";
}
    
getBollywood(): string {
    return "Bramastra";
}
}

class EnglishAudience implements Movies{

    getBollywood(): string {
        return "not interested";
    }
    getHollywood(): string {
        return "Tenet";
    }

}


let ha=new HindiAudience();
let ea=new EnglishAudience();
console.log("Favourite Hindi movie :",ha.getBollywood());
console.log( "Favourite English Movie :",ea.getHollywood());






/*interface Json
{
    toJSON():string;
}

class Student implements Json
{
    constructor(private name:string,private age:number)
    {

    }
    toJSON(): string {
        return JSON.stringify(this);
    }
    
}


let st1=new Student("Rahul",26);
console.log(st1);

*/
