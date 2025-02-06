import React, { createContext, useEffect, useState } from 'react';

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
    const [accessToken, setAccessToken] = useState(null);
    const [userEmail, setUserEmail] = useState(null);

    useEffect(() => {
        const token = localStorage.getItem('access_token');
        const email = localStorage.getItem('email');

        if (token && email) {
            setAccessToken(token);
            setUserEmail(email);
        };
        console.log(email)
    }, []);

    return (
        <AuthContext.Provider value={{ accessToken, userEmail, setAccessToken, setUserEmail }}>
            {children}
        </AuthContext.Provider>
    );
};
