
export async function getData({id}){
  const response = await fetch(`http://127.0.0.1:8000/${id}`);
  if (!response.ok) {
      throw new Error(`Error! status: ${response.status}`);
  }

  return response.json()
}


export default async function Article({id}) {
  const data = await getData({id});

  if (!data) {
      return <p>Loading...</p>
  }


  return (
<div className="max-w-2xl mx-auto my-8">
      <h1 className="text-4xl font-bold mb-4">{data.data.title}</h1>
      <p className="text-gray-600 mb-2">
         {data.data.published_date}
      </p>
      {data.data.url && (
        <a
          href={data.data.url}
          target="_blank"
          rel="noopener noreferrer"
          className="text-blue-500 hover:underline"
        >
          Source
        </a>
      )}
    {data.data.type && (
        <p className="text-gray-600 mb-2">
          Type: {data.data.type.name}
        </p>
      )}
      {data.data.authors && (
        <p className="text-gray-600">
          Author: {data.data.authors.map(author => author.full_name).join(', ')}
        </p>
      )}
      <p className="mb-5 mt-5">{data.data.short_desc}</p>
      {data.data.content && <p className="mb-5 mt-5">{data.data.content}</p>}

    </div>
  );
}