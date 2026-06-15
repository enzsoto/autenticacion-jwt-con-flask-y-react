import React from "react";

export const Private = () => {
    return (
        <div className="container mt-5">
            <div className="row justify-content-center">
                <div className="col-12 col-md-8">
                    <div className="card shadow-sm">
                        <div className="card-body text-center">
                            <h1 className="mb-3">Página privada</h1>
                            <p className="lead">
                                Entraste a tu página privada.
                            </p>
                            <p>
                                Esta vista solo debería ser accesible si tienes sesión iniciada.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};