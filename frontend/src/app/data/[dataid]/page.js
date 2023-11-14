import Article from "@/components/GetArticle";


export default function ProductDetail({params}){
    return (
      <div>
        <Article id={params.dataid}/>
      </div>
  )
}