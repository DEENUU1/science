import Link from "next/link";

export async function getListData() {
  const response = await fetch('http://127.0.0.1:8000');

  if (!response.ok) {
      throw new Error(`Error! status: ${response.status}`);
  }

  return response.json()
}


export default async function ArticleList() {
  const datas = await getListData();
  return (
    <ul>
      {datas.data?.map((data) => (
        <li key={data.id}>
          <h3>{data.title}</h3>
          <p>{data.short_desc}</p>
          <a href={data.url}>{data.url}</a>
          <Link href={`/data/${data.id}`}>Full content</Link>
        </li>
      ))}
    </ul>
  );
}