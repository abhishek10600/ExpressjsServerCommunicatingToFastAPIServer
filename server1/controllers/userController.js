import axios from "axios"

export const registerUser = async (req, res, next) => {
    try {
        const { name, email, password } = req.body;
        const response = await axios.post("http://127.0.0.1:8000/user/get-data", {
            name,
            email,
            password
        })
        console.log(response.data)
        res.status(201).json({
            success: true,
            message: "user created successfully.",
            userData: {
                name,
                email,
                password
            }
        })
    } catch (error) {
        console.log(error);
    }
}
