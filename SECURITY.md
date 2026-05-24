# Security Notes

LifeCore creates local signing keys for runtime use. Generated private key files such as `lifecore.key` are intentionally ignored by Git and must not be committed, published, or shared.

If a real private key was ever committed to a public repository, treat it as compromised. Remove it from the repository, rotate or regenerate the key, and update any environment or device that relied on the old key.

For normal local development, run the application without copying a key into the repository. The application will create a fresh local `lifecore.key` when needed.
