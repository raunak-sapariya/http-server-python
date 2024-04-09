const express=express()

const syllabusRouter=express.Router()

syllabusRouter.get("/all",getAllSyllabus)

module.exports={
    syllabusRouter
}