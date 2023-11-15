'use client'


import Link from "next/link";
import { useState, useEffect } from "react";
import {stringify} from "postcss";
// import { useRouter } from "next/router";

const Navbar = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [user, setUser] = useState(null);
  // const router = useRouter();

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
          // router.push("/");
        }
      };

      fetchData();
    }
  }, []);

  const handleLogout = () => {
    localStorage.removeItem("token");
    setIsLoggedIn(false);
    // router.push("/");
  };

  return (
    <div className="navbar bg-base-100">
      <div className="flex-1">
        <a className="btn btn-ghost normal-case text-xl">Science</a>
      </div>
      <div className="flex-none">
        <ul className="menu menu-horizontal px-1">
          <li>
            <Link href="/">Home</Link>
          </li>
          {isLoggedIn && (
            <>
              <li>
                {user && <span>Welcome, {user.first_name}!</span>}
              </li>
              <li>
                <Link href="#" onClick={handleLogout}>Logout</Link>
              </li>
            </>
          )}
        </ul>
      </div>
    </div>
  );
};

export default Navbar;
