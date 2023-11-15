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
    <div className="grid h-screen place-items-center">
      <h1 className="text-4xl mb-5 ">{datas.count} articles available to read</h1>
        {datas.data?.map((data) => (
          <div key={data.id} className="max-w-lg  p-6 bg-white border border-gray-400 rounded-lg  dark:bg-gray-800 dark:border-gray-700 mb-5 shadow-lg rounded-lg">
            <Link  href={data.url}>
              <h3 className="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">{data.title}</h3>
            </Link>
           <blockquote  className="mb-3 italic text-left text-gray-900 dark:text-white">{data.short_desc}</blockquote >
            <Link className="inline-flex items-center px-3 py-2 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800" href={`/${data.id}`}>
                Full content
                <svg className="rtl:rotate-180 w-3.5 h-3.5 ms-2" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 10">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M1 5h12m0 0L9 1m4 4L9 9"/>
                </svg>
            </Link>
          </div>
        ))}
    </div>
  );
}