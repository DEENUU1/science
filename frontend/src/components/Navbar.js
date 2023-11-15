'use client'

import Link from "next/link";
import { useState, useEffect } from "react";
import Image from 'next/image';

const Navbar = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [user, setUser] = useState(null);
  const [navbar, setNavbar] = useState(false);

  useEffect(() => {
    if (localStorage.getItem("token")) {
      setIsLoggedIn(true);

      const fetchData = async () => {
        const response = await fetch("http://127.0.0.1:8000/auth/user", {
          method: "GET",
          headers: {
            "accept": "application/json",
            "token":`${localStorage.getItem("token")}`,
            "Access-Control-Allow-Origin": "*",
          },

        });

        if (response.ok) {
          const userData = await response.json();
          setUser(userData);
        } else {
          localStorage.removeItem("token");
          setIsLoggedIn(false);
        }
      };

      fetchData();
    }
  }, []);

  const handleLogout = () => {
    localStorage.removeItem("token");
    setIsLoggedIn(false);
  };

  return (
    <div>
      <nav className="w-full bg-black fixed top-0 left-0 right-0 z-10">
        <div className="justify-between px-4 mx-auto lg:max-w-7xl md:items-center md:flex md:px-8">
          <div>
            <div className="flex items-center justify-between py-3 md:py-5 md:block">
              <Link href="/">
                <h2 className="text-2xl text-cyan-600 font-bold "><Image width={50} height={50} src="https://img.freepik.com/darmowe-wektory/projekt-szablonu-logo-nauki_23-2150337872.jpg?w=1380&t=st=1700078773~exp=1700079373~hmac=1b262ef35470542b75e168f46f8a5ade8554a1ac43a6c75566087b4f83442fb9"></Image> </h2>
              </Link>
              {/* HAMBURGER BUTTON FOR MOBILE */}
              <div className="md:hidden">
                <button
                  className="p-2 text-gray-700 rounded-md outline-none focus:border-gray-400 focus:border"
                  onClick={() => setNavbar(!navbar)}
                >
                  {navbar ? (
                    <Image src="/icons8-close.svg" width={30} height={30} alt="logo" />
                  ) : (
                    <Image
                      src="/icons8-menu.svg"
                      width={30}
                      height={30}
                      alt="logo"
                      className="focus:border-none active:border-none"
                    />
                  )}
                </button>
              </div>
            </div>
          </div>
          <div>
            <div
              className={`flex-1 justify-self-center pb-3 mt-8 md:block md:pb-0 md:mt-0 ${
                navbar ? 'p-12 md:p-0 block' : 'hidden'
              }`}
            >
              <ul className="h-screen md:h-auto items-center justify-center md:flex ">
               {isLoggedIn ? (
                  <>
                    <li className="pb-6 text-xl text-white py-2 px-6 text-center  border-b-2 md:border-b-0  hover:bg-blue-400  border-blue-900  md:hover:text-blue-600 md:hover:bg-transparent">
                      <Link href="#" onClick={() => setNavbar(!navbar)}>
                        Welcome, {user.first_name}
                      </Link>
                    </li>
                    <li className="pb-6 text-xl text-white py-2 px-6 text-center  border-b-2 md:border-b-0  hover:bg-blue-400  border-blue-900  md:hover:text-blue-600 md:hover:bg-transparent">
                      <Link href="#" onClick={handleLogout}>
                        Logout
                      </Link>
                    </li>
                  </>
                ) : (
                  <>
                    <li className="pb-6 text-xl text-white py-2 px-6 text-center  border-b-2 md:border-b-0  hover:bg-blue-400  border-blue-900  md:hover:text-blue-600 md:hover:bg-transparent">
                      <Link href="/user/login" onClick={() => setNavbar(!navbar)}>
                        Login
                      </Link>
                    </li>
                    <li className="pb-6 text-xl text-white py-2 px-6 text-center  border-b-2 md:border-b-0  hover:bg-blue-400  border-blue-900  md:hover:text-blue-600 md:hover:bg-transparent">
                      <Link href="/user/register" onClick={() => setNavbar(!navbar)}>
                        Register
                      </Link>
                    </li>
                  </>
                )}
              </ul>
            </div>
          </div>
        </div>
      </nav>
    </div>
  );
};

export default Navbar;
