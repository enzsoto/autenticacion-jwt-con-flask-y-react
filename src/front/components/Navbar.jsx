import React, { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";

export const Navbar = () => {
	const navigate = useNavigate();
	const [isLoggedIn, setIsLoggedIn] = useState(
		!!sessionStorage.getItem("token")
	);

	useEffect(() => {
		const checkAuth = () => {
			setIsLoggedIn(!!sessionStorage.getItem("token"));
		};

		window.addEventListener("authChange", checkAuth);

		return () => {
			window.removeEventListener("authChange", checkAuth);
		};
	}, []);

	const handleLogout = () => {
		sessionStorage.removeItem("token");
		sessionStorage.removeItem("user");

		setIsLoggedIn(false);

		navigate("/login");
	};

	return (
		<nav className="navbar navbar-light bg-light">
			<div className="container">
				<Link to="/" className="text-decoration-none">
					<span className="navbar-brand mb-0 h1">React Boilerplate</span>
				</Link>

				<div className="ms-auto d-flex gap-2">
					{isLoggedIn ? (
						<>
							<Link to="/private">
								<button className="btn btn-success">Private</button>
							</Link>

							<button
								className="btn btn-outline-danger"
								onClick={handleLogout}
							>
								Cerrar sesión
							</button>
						</>
					) : (
						<>
							<Link to="/login">
								<button className="btn btn-outline-primary">Login</button>
							</Link>

							<Link to="/signup">
								<button className="btn btn-primary">Sign up</button>
							</Link>
						</>
					)}
				</div>
			</div>
		</nav>
	);
};