var Seller = /** @class */ (function () {
    function Seller() {
    }
    Seller.prototype.check = function (itemCount) {
        do {
            console.log(itemCount);
            itemCount++;
        } while (itemCount <= 5);
        /*while(itemCount<=5)
        {
          console.log(itemCount);
          itemCount++;
        }*/
        /*for(initialization;condition;expression)
        for (let i=0;i<itemCount;i++){
            console.log(`You got ${i} coupon to redeem on purchase of ${i+500}`);
        }*/
        /* Implementing switch statements
        let discount:number;
         switch(itemCount)
         {
             case 5:
                 discount=5;
                 break;
                 case 10:
                 discount=10;
                 break;
                 case 15:
                 discount=15;
                 break;
                 default:
                     discount=20;
                     break;
     
     
     
         }
         console.log(`you got ${discount}% discount on your order`);
         */
        /*Implementing if-else
    
        let discount :number;
        if(itemCount >= 1 && itemCount <=5)
        {
            discount=5;
        }
        else if (itemCount > 5 && itemCount <=10)
        {
            discount=10;
        }
        else if (itemCount > 10 && itemCount <15)
        {
            discount=15;
        }
        else{
            discount=20;
        }
    
        console.log(`you got ${discount}% discount on your order`);
        */
    };
    return Seller;
}());
var seller1 = new Seller();
seller1.check(6);
