
export async function getData({id}){
  const response = await fetch(`http://127.0.0.1:8000/${id}`);
  if (!response.ok) {
      throw new Error(`Error! status: ${response.status}`);
  }

  return response.json()
}


export default async function Article({id}) {
  const data = await getData({id});
  return (
    <ul>
      <h1>{data.data.title}</h1>
      <a href={data.data.url}>Full content</a>
      <span>{data.data.published_date}</span>
      {/*<span>{data.data.type}</span>*/}
      {/*<span>{data.data.authors}</span>*/}
      <p>{data.data.short_desc}</p>
      <p>{data.data.content}</p>

    </ul>
  );
}