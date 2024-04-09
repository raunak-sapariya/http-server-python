const _getSyllabus=async()=>{
    try{
    const q=`SELECT c.*,sc.*,p.*,pp.* FROM categories c 
    JOIN subcategories sc ON c.category_id=sc.category_id 
    JOIN problems p ON sc.id=p.subcategory_id 
    JOIN parts_of_problem pp ON p.id=pp.problem_id`
    const [rows]=pool.query(q)
    return formatData(rows)
    }catch(err){
        console.log(err)
    }
}