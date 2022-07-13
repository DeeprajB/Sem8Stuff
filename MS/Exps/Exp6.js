const readline = require("readline").createInterface({
    input: process.stdin,
    output: process.stdout
})
function sstf(start,jobs){ 
    let totalDistance=0
    let jobOrder=[]
    let currPos=start
    while(jobs.length>0){
           let closestIdx=-1
           let smallestDistance=Infinity
           for(let i=0;i<jobs.length;i++){
                   let currDist=Math.abs(currPos-jobs[i])
                   if(currDist<smallestDistance){
                          smallestDistance=currDist
                          closestIdx=i
} }
           jobOrder.push(jobs[closestIdx])
           totalDistance+=Math.abs(currPos-jobs[closestIdx])
           currPos=jobs[closestIdx]
           jobs.splice(closestIdx,1)
    }
    console.log("Total distance seeked: ",totalDistance)
    console.log("seek order:")
    for(let i=0;i<jobOrder.length;i++){
           console.log(jobOrder[i])
} }
async function getJobs(){
    let joblist= await new Promise(resolve=>{
           readline.question("Enter job addresses separated by spaces:\n",
               resolve)
    })
    return joblist.split(" ")
}
async function getStart(){
    let start=await new Promise(resolve=>{
                   readline.question("Enter the start address of disk head\n",
                   resolve)
    
}) 
return Number(start)}
               

const main = async() => {
           let jobs=await getJobs()
           let start=await getStart()
           sstf(start,jobs)
    process.exit(0)
} 
main()