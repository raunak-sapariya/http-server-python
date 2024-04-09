const fs=require("fs")
let count;
fs.readFile("a.txt",(err,data)=>{
    if (err)console.log(err)
    data=data+data
fs.writeFile("a.txt",data.toString(),(err)=>{
    console.log("asdjfdsaf"+data)
})
})