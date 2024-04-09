const r_getSyllabus=async()=>{
    try{
    const key="all_syllabus"
    const cache=await getVal(key)
    return JSON.parse(cache)
}catch(err){
    console.log(err)
    return undefined
}
}


const r_setSyllabus=async(value)=>{
    try{
    const key="all_syllabus"
    const result=await setVal(key,value)
    return result
}catch(err){
    console.log(err)
    return undefined
}
}






const getVal=async()=>{
    try {
        const cache=await redisClient.get(key)
        return cache
    } catch (err) {
        console.log(err)
    }
}

const setVal=async(key,value)=>{
    try{
    const res=await redisClient.set(key,value)
    return res
    }catch(err){
        console.log(err)
    }
}
