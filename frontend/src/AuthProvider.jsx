import React, { createContext, useEffect, useState } from 'react';

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
    const [accessToken, setAccessToken] = useState(null);
    const [userEmail, setUserEmail] = useState(null);

    useEffect(() => {
        const token = localStorage.getItem('accessToken');
        const email = localStorage.getItem('email');

        if (token && email) {
            setAccessToken(token);
            setUserEmail(email);
        };
        
    }, []);

    return (
        <AuthContext.Provider value={{ accessToken, userEmail, setAccessToken, setUserEmail }}>
            {children}
        </AuthContext.Provider>
    );
};
