import React, { useState } from 'react';

const InputField = () => {
    const [inputValue, setInputValue] = useState('');

    const handleInputChange = (e) => {
        setInputValue(e.target.value);
    };

    return (
        <div className="input-container">
            <label htmlFor="input">INPUT</label>
            <input
                id="input"
                type="text"
                value={inputValue}
                onChange={handleInputChange}
            />       
        </div>
        
    );
};

export default InputField;