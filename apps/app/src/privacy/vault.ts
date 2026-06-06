export type VaultContact = {
  realName?: string;
  phone?: string;
  address?: string;
};

export interface PiiVault {
  getContact(): Promise<VaultContact | null>;
  setContact(contact: VaultContact): Promise<void>;
  clear(): Promise<void>;
}
