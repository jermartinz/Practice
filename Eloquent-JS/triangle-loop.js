
let character = '#'


for(let char = '#'; char.length < 8; char += '#'){
    console.log(char);
}
/* #
    ##
    ###
    ####
    #####
    ######
    ####### 
*/

for (let number = 0; number <= 100; number++) {
    if (number % 15 === 0) {
        console.log('FizzBuzz');
    }else if(number % 5 === 0 && number % 3 != 0){
        console.log('Buzz')
    }else if (number % 3 === 0){
        console.log('Fizz')
    }else{
        console.log(number)
    }
    
}

