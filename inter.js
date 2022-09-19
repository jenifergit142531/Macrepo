var HindiAudience = /** @class */ (function () {
    function HindiAudience() {
    }
    HindiAudience.prototype.getHollywood = function () {
        return "not imterested";
    };
    HindiAudience.prototype.getBollywood = function () {
        return "Bramastra";
    };
    return HindiAudience;
}());
var EnglishAudience = /** @class */ (function () {
    function EnglishAudience() {
    }
    EnglishAudience.prototype.getBollywood = function () {
        return "not interested";
    };
    EnglishAudience.prototype.getHollywood = function () {
        return "Tenet";
    };
    return EnglishAudience;
}());
var ha = new HindiAudience();
var ea = new EnglishAudience();
console.log("Favourite Hindi movie :", ha.getBollywood());
console.log("Favourite English Movie :", ea.getHollywood());
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
