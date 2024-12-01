class FormToggle extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            isSignup: true,
        };
    }

    toggleForm = () => {
        this.setState({ isSignup: !this.state.isSignup });
    };

    render() {
        return (
            <div className="col-md-4">
                {this.state.isSignup ? (
                    <div id="signup-form" className="border p-4 rounded bg-light">
                        <h3 className="text-center">Signup Form</h3>
                        <form>
                            <div className="mb-3">
                                <input
                                    type="email"
                                    className="form-control"
                                    placeholder="Email Address"
                                    required
                                />
                            </div>
                            <div className="mb-3">
                                <input
                                    type="password"
                                    className="form-control"
                                    placeholder="Password"
                                    required
                                />
                            </div>
                            <div className="mb-3">
                                <input
                                    type="password"
                                    className="form-control"
                                    placeholder="Confirm Password"
                                    required
                                />
                            </div>
                            <button type="submit" className="btn btn-danger w-100">
                                Sign Up
                            </button>
                        </form>
                        <p className="text-center mt-3">
                            Already have an account?{" "}
                            <a href="#" onClick={this.toggleForm}>
                                Login now
                            </a>
                        </p>
                    </div>
                ) : (
                    <div id="login-form" className="border p-4 rounded bg-light">
                        <h3 className="text-center">Login Form</h3>
                        <form>
                            <div className="mb-3">
                                <input
                                    type="email"
                                    className="form-control"
                                    placeholder="Email Address"
                                    required
                                />
                            </div>
                            <div className="mb-3">
                                <input
                                    type="password"
                                    className="form-control"
                                    placeholder="Password"
                                    required
                                />
                            </div>
                            <button type="submit" className="btn btn-danger w-100">
                                Login
                            </button>
                        </form>
                        <p className="text-center mt-3">
                            Don’t have an account?{" "}
                            <a href="#" onClick={this.toggleForm}>
                                Sign up now
                            </a>
                        </p>
                    </div>
                )}
            </div>
        );
    }
}

ReactDOM.render(<FormToggle />, document.getElementById("react-root"));
