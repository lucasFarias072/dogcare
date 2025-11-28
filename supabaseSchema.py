

# Exemplo em produção
class Schema:
    """
    -- Criar tabela de tutores (profiles)
    CREATE TABLE profiles (
        id UUID REFERENCES auth.users(id) PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
        updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );

    -- Criar tabela de pets
    CREATE TABLE pets (
        id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
        owner_id UUID REFERENCES profiles(id) ON DELETE CASCADE NOT NULL,
        name TEXT NOT NULL,
        breed TEXT NOT NULL,
        birth_date DATE NOT NULL,
        created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
        updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );

    -- Habilitar RLS (Row Level Security)
    ALTER TABLE profiles ENABLE ROW LEVEL SECURITY;
    ALTER TABLE pets ENABLE ROW LEVEL SECURITY;

    -- Políticas de segurança para profiles
    CREATE POLICY "Usuários podem ver seu próprio perfil"
    ON profiles FOR SELECT
    USING (auth.uid() = id);

    CREATE POLICY "Usuários podem atualizar seu próprio perfil"
    ON profiles FOR UPDATE
    USING (auth.uid() = id);

    CREATE POLICY "Usuários podem inserir seu próprio perfil"
    ON profiles FOR INSERT
    WITH CHECK (auth.uid() = id);

    -- Políticas de segurança para pets
    CREATE POLICY "Usuários podem ver seus próprios pets"
    ON pets FOR SELECT
    USING (auth.uid() = owner_id);

    CREATE POLICY "Usuários podem criar pets"
    ON pets FOR INSERT
    WITH CHECK (auth.uid() = owner_id);

    CREATE POLICY "Usuários podem atualizar seus próprios pets"
    ON pets FOR UPDATE
    USING (auth.uid() = owner_id);

    CREATE POLICY "Usuários podem deletar seus próprios pets"
    ON pets FOR DELETE
    USING (auth.uid() = owner_id);

    -- Função para criar perfil automaticamente após registro
    CREATE OR REPLACE FUNCTION public.handle_new_user()
    RETURNS TRIGGER AS $$
    BEGIN
    INSERT INTO public.profiles (id, email, name)
    VALUES (
        NEW.id,
        NEW.email,
        COALESCE(NEW.raw_user_meta_data->>'name', split_part(NEW.email, '@', 1))
    );
    RETURN NEW;
    END;
    $$ LANGUAGE plpgsql SECURITY DEFINER;

    -- Trigger para criar perfil automaticamente
    CREATE TRIGGER on_auth_user_created
    AFTER INSERT ON auth.users
    FOR EACH ROW EXECUTE FUNCTION public.handle_new_user();
    """

# Exemplo local
class SchemaSimplificado:
    """
    -- Tabela de tutores (SEM RLS)
    CREATE TABLE profiles (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
    );

    -- Tabela de pets (SEM RLS)
    CREATE TABLE pets (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    owner_id UUID REFERENCES profiles(id) ON DELETE CASCADE,
    name TEXT NOT NULL,
    breed TEXT NOT NULL,
    birth_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
    );
    """

class Dependencias:
    """
    npm install @supabase/supabase-js
    """

class Env:
    """
    VITE_SUPABASE_URL=https://ccnlhopylxadrcbytaog.supabase.co
    VITE_SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNjbmxob3B5bHhhZHJjYnl0YW9nIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjQyODgzODQsImV4cCI6MjA3OTg2NDM4NH0.mOZmluy11bAQrxURmfchUW8lrYWEKOW_8C79V0GE3t4
    """

# Criação manual
class SupabaseClient:
    """
    app/supabaseClient.ts
    """

# Criação manual (está com erro)
"""
'ReactNode' is a type and must be imported using a type-only import when 'verbatimModuleSyntax' is enabled.
"""
class AuthContext:
    """
    app/AuthContext.tsx
    """

# Criado manualmente
class ProtectedRoute:
    """
    app/ProtectedRoute.tsx
    """

# Atualizado (problema)
# Cannot redeclare exported variable 'default'.
# Duplicate function implementation.
class Root:
    """
    atualizações
    """

class PetOwnerForm:
    """
    atualizações
    """

# Atualizado (problemas)
# Property 'success' does not exist on type 'Boolean'.
# Property 'error' does not exist on type 'Boolean'.
class Login:
    """
    atualizações
    """

# Atualizado (problemas)
# All imports in import declaration are unused.
# 'Pet' is a type and must be imported using a type-only import when 'verbatimModuleSyntax' is enabled.
# All destructured elements are unused.
# Property 'profile' does not exist on type 'AuthContextType'.
class PetOwnerPanel:
    """
    atualizações
    """

class Gitignore:
    """
    atualizações
    """

class ModificacaoSupabaseNaoConfirmarEmail:
    """
    Authentication >> Sign-in/Providers >> Confirm email (desabilitar) >> save changes
    """
